// 문자열 길이 순으로 정렬
slist = slist.sort((x,y)=>x.length-y.length)
//배열 filter
score.filter(x => x > 80)
//내림차순
result.sort((a, b) => {
    return b-a;
    });

function gcdlcm(a, b) {
    var answer = [];
    var minNum = Math.min(a, b);
    var maxNum = Math.max(a, b);
    answer[0] = gcd(minNum, maxNum);
    answer[1] = lcm(minNum, maxNum);
    return answer;
}
// 최대공약수
function gcd(minNum, maxNum){
  return (minNum % maxNum) === 0 ? maxNum : gcd(maxNum, minNum % maxNum);
}
// 최소공배수
function lcm(minNum, maxNum){
  return minNum * maxNum / gcd(minNum, maxNum);
}

// sort by value
const mapSort1 = new Map([...myMap.entries()].sort((a, b) => b[1] - a[1]));
console.log(mapSort1);
// Map(4) {"c" => 4, "a" => 3, "d" => 2, "b" => 1}

const mapSort2 = new Map([...myMap.entries()].sort((a, b) => a[1] - b[1]));
console.log(mapSort2);
// Map(4) {"b" => 1, "d" => 2, "a" => 3, "c" => 4}

// sort by key
const mapSort3 = new Map([...myMap.entries()].sort());
console.log(mapSort3);
// Map(4) {"a" => 3, "b" => 1, "c" => 4, "d" => 2}

const mapSort4 = new Map([...myMap.entries()].reverse());
console.log(mapSort4);
// Map(4) {"d" => 2, "b" => 1, "c" => 4, "a" => 3}

// 10진수->3진법
[...n.toString(3)]

// 3진법->10진수
parseInt([...n.toString(3)].join(''),3)
