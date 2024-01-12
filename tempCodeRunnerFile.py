if ((math.dist((o_x*x,o_y*y),(i*x,j*y)))<=r):
            res[(i,j)]=(round(i*x*1.0,4),round(j*y*1.0,4))
            res[(-1*i,j)]=(round(i*x*1*-1.0,4),round(j*y*1.0,4))
            res[(i,-1*j)]=(round(i*x*1.0,4),round(j*y*-1*1.0,4))
            res[(-1*i,-1*j)]=(round(i*x*-1.0,4),round(j*y*-1.0,4))