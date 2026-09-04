def parse_flags(args: list[str]) -> dict[str,object]:
    """Parse simple --key value and --flag command-line arguments."""
    out={}; i=0
    while i<len(args):
        token=args[i]
        if not token.startswith('--'): raise ValueError(f'expected flag: {token}')
        key=token[2:]
        if not key: raise ValueError('empty flag')
        if i+1<len(args) and not args[i+1].startswith('--'): out[key]=args[i+1]; i+=2
        else: out[key]=True; i+=1
    return out
