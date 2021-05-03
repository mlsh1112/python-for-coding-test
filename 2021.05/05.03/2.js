function solution(stones, k) {
    return bs(stones,k,0,200000000)
}

const bs=(stones,k,min,max)=>{
    if(min===max){ return min}
    let mid = Math.round((min+max)/2)
    let result=0
    
    for(let i=0;i<stones.length;i++){
        if(result===k){
            break
        }
        let stone=stones[i]-(mid-1)
        stone<=0?result++:result=0
    }
    if(result===k) {return bs(stones,k,min,mid-1)}
    else {return bs(stones,k,mid,max)}
    
}