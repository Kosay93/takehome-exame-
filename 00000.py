



def compare (v:List[int],n:int)->tuple[int,int,int]:
    if v==[]:
        return(0, 0, 0)
    else:
        (gt,eq,lt)=compare (v[1:],n)
        if v[0]=>n:
            return (gt+1,eq,lt)
        elif v[0]==n:
            return (gt,eq+1,lt)
        else:
            return (gt,eq,lt+1)
        
        
            
