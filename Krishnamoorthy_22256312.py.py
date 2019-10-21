def trackProjectile(vx,vy,g):
    time=0.0
    sx= vx*time
    sy= vy*time+((g*time*time)/2)
    vyn=0
    a=[]
    b=[]
    c=[]
    d=(c,b,a)
    while sy>=0:
        a.append(round(time,2))
        b.append(round(sy,2))
        c.append(round(sx,2))
        time=time+0.1
        vyn=vy+0.1*g
        sy=sy+0.1*(vy+vyn)/2
        sx=sx+0.1*(vx+vx)/2
        vy=vyn
        if sy<0:
            break
    return d