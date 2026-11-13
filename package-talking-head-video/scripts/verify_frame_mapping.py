"""Validate ordered unit-speed, constant-FPS cuts against decoded video frames."""
import argparse
import json
import subprocess


def audit_mapping(rows):
    if not isinstance(rows, list) or not rows:
        raise ValueError('Mapping must be a nonempty list of unit-speed frame spans')
    cursor = 0
    spans = []
    revisits = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ValueError(f'Clip {index}: expected an object')
        keys = ('start', 'end', 'in', 'out')
        if any(type(row.get(key)) is not int for key in keys):
            raise ValueError(f'Clip {index}: frame boundaries must be integers')
        start, end, first, stop = (row[key] for key in keys)
        if start != cursor or end <= start or first < 0 or stop <= first:
            raise ValueError(f'Clip {index}: gap, overlap in timeline or invalid span')
        if end - start != stop - first:
            raise ValueError(f'Clip {index}: unsupported non-unit-speed mapping')
        if any(first < old_stop and stop > old_first for old_first, old_stop in spans):
            revisits.append(index)
        spans.append((first, stop))
        cursor = end
    return {'expectedVideoFrames': cursor, 'sourceReuseClipIndices': revisits}


def compare_count(report, actual):
    if actual != report['expectedVideoFrames']:
        raise ValueError(f"Video frame mismatch: expected {report['expectedVideoFrames']}, decoded {actual}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mapping', required=True)
    parser.add_argument('--video', required=True)
    parser.add_argument('--ffprobe', default='ffprobe')
    args = parser.parse_args()
    try:
        with open(args.mapping, encoding='utf-8-sig') as handle:
            report = audit_mapping(json.load(handle))
        result = subprocess.run([
            args.ffprobe, '-v', 'error', '-select_streams', 'v:0',
            '-count_frames', '-show_entries',
            'stream=nb_read_frames,avg_frame_rate,r_frame_rate,width,height',
            '-of', 'json', args.video,
        ], check=True, capture_output=True, text=True)
        if result.stderr.strip():
            raise ValueError('Decoder reported errors: ' + result.stderr.strip())
        stream = json.loads(result.stdout)['streams'][0]
        actual = int(stream['nb_read_frames'])
        compare_count(report, actual)
        report.update(actualVideoFrames=actual, stream=stream,
                      scope='Frame counts only; verify FPS, mapped pixels and lip sync separately')
        print(json.dumps(report, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, IndexError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'FAIL: {error}\n')


if __name__ == '__main__':
    main()
