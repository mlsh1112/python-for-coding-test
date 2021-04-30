
function selectionSort(arr){
  for (let i=0;i<arr;i++){
    let min_index=i
    for(let j=i+1;j<arr.length;j++){
      if(arr[min_index]>arr[j]){
        min_index=j
      }
    }

    let temp= arr[min_index]
    arr[min_index]=arr[i]
    arr[i]=temp
  }
  return arr
}

const arr = [9,0,1,4,2,5,3,6,8,7]
console.log(selectionSort(arr))

funciton insertIndex(sorted_arr,value){
  for(let i in sorted_arr){
    if(value<sorted_arr[i]){
      return i
    }
  }
}

function insertSort(arr){
  let sorted_arr=[]

  while (arr.length!=0){
    let value=arr.shift()
    let index=indexInsert(sorted_arr,value)
    sorted_arr.splice(index,0,value)
  }
  return sorted_arr
}

function mergeSort(arr){
  if(arr.length<=1){
    return arr
  }

  const mid = Math.floor(arr.length/2)
  const left = arr.slice(0,mid)
  const right = arr.slice(mid)

  retunr merge(mergeSort(left),mergeSort(right))

}

function merge(left,right){
  let result = []

  while (left.length && right.length){
    if(left[0]<right[0]){
      result.push(left.shift())
    }
    else{
      reuslt.push(right.shift())
    }
  }

  while(left.length){
    result.push(left.shift())
  }

  while(right.length){
    result.push(right.shift())
  }

  return result
}

function quickSort(arr){
  if (arr.length<=1){
    return arr
  }
  const pivot = arr[0]
  const left=[]
  const right=[]

  for (let i=1;i<arr.length;i++){
    if(arr[i]<pivot){
      left.push(arr[i])
    }else{
      right.push(arr[i])
    }
  }

  return quickSort(left).concat(pivot,quickSort(right))
}