function cal(arr,math){
    var result=arr[0]
    if(math==='*'){
        for(let i=1;i<arr.length;i++)
            result*=arr[i]
    }
    else if(math==='+'){
        for(let i=1;i<arr.length;i++)
            result+=arr[i]
    }
    else if(math==='-'){
        for(let i=1;i<arr.length;i++)
            result-=arr[i]
    }
    return result
}
function solution(expression) {
    var answer = 0;
    var result=[]
    const maths =[
        ['*','+','-'],
        ['*','-','+'],
        ['+','*','-'],
        ['+','-','*'],
        ['-','*','+'],
        ['-','+','*']
    ]
    
    for (let math of maths){
        const arr= expression.split(math[0])
        for(let i=0;i<arr.length;i++){
            const arr2=arr[i].split(math[1])
            for(let j=0;j<arr2.length;j++){
                arr2[j]=eval(arr2[j])
            }
            arr[i]=cal(arr2,math[1])
        }
        result.push(Math.abs(cal(arr,math[0])))
    }
    result.sort((a, b) => {
    return b-a;
    });
    answer=result[0]
    return answer;
}