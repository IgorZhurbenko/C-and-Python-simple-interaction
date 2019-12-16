import subprocess as sb

def OnesWithin(a,b):
    with sb.Popen(["5", str(a), str(b), "rm", "r"],executable="a.exe") as proc:
        return proc.wait()
        
a,b = input().split();
print([a,b]);
print("Result is", OnesWithin(a,b))
