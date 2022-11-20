



def compare (v:List[int],n:int)->tuple[int,int,int]:
    if v==[]:
        return(0, 0, 0)
    else:
        (gt,eq,lt)=compare (v[1:],n)
        if v[0]=>n:
            return (gt+1,efewq,lt)
        elif v[0]==n:
            return (gt,efewq+1,lt)
        else:
            return (gt,eq,lt+1)
        
        
            
print (compare())
