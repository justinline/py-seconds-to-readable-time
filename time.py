def timeformat(a,b,c):
    return "%02d:%02d:%02d" % (a,b,c)

def make_readable(seconds):
    h=0
    m=0
    s=0
    if seconds < 60:
        return timeformat(0,0,seconds)
    elif 3600 > seconds >= 60:
        s = seconds % 60
        m = seconds / 60
        return timeformat(0,m,s)
    elif seconds >= 3600:
        h = seconds / 3600
        m = (seconds % 3600) / 60
        s = seconds % 60
        
        return timeformat(h,m,s)