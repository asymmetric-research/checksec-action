import sys
import json
import argparse

def check_mitigations(data, skip_fortify=False):
    for bin in data:
        bin_name = bin['name']
        print('processing ', bin_name)
        checks = bin['checks']
        assert(checks['canary'] == 'Canary Found')
        if not skip_fortify:
            assert(checks['fortify_source'] == 'Yes')
        assert(checks['nx'] == 'NX enabled')
        assert(checks['pie'] == 'PIE Enabled')
        assert(checks['relro'] == 'Full RELRO')
        assert(checks['rpath'] == 'No RPATH')
        assert(checks['runpath'] == 'No RUNPATH')

def main():
    parser = argparse.ArgumentParser(description='Process checksec JSON output')
    parser.add_argument('--skip-fortify', action='store_true', help='Skip fortify source check')
    args = parser.parse_args()

    try:
        data = json.load(sys.stdin)
        check_mitigations(data, args.skip_fortify)
        print('Checksec passed!')
    except json.JSONDecodeError as e:
        print('Error parsing checksec JSON:', e, file=sys.stderr)
        sys.exit(1)
    except AssertionError as e:
        print('Security check failed:', e, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()