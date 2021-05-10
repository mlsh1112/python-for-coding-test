function solution(s) {
    var answer = 0;
    var lengths=[]
    lengths.push(s.length)
    answer= slice(s,0,s.length,s.length)
    
    function slice(s,min,max,length){
        if(min===max) {return length}
        //잘린 문자열을 넣을 stack
        var slices=[]
        //문자열의 중간 길이
        var len=Math.round((max+min)/2)
        var same=1
        
        for(let i=0;i<s.length;i+=len){
            if(slices.length===0){
                slices.push(s.slice(i,i+len))
                continue
            }
            
            var exs=slices.pop()
            if(s.slice(i,i+len)!==exs){
            //이전 문자가 같다가 달라지면 같은 문자의 개수와 문자를 push한다.
            if(same>1){
                slices.push(same)
            }
              same=1
              slices.push(exs)
              slices.push(s.slice(i,i+len))
              continue
            }
            //문자가 동일할 경우
            else if(s.slice(i,i+len)===exs){
                same+=1
              if(i+len===s.length){
                  slices.push(same)
              }
                slices.push(exs)
            }
        }
        //총 문자열의 길이
        var sliceslen=0
        for(let j=0;j<slices.length;j++){
            slices[j]=String(slices[j])
            sliceslen+=slices[j].length
        }
         
         lengths.push(sliceslen)
        
         slice(s,len,max,length)
         slice(s,min,len-1,length)
        
        return
    }
    //가장 짧은 문자열의 길이를 return 한다.
    lengths.sort((a,b)=>a-b)
    
    return lengths[0];
}