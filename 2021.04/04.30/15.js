//queue
class Queue {
  constructor(){
    this._arr=[]
  }
  enqueue(item){
    this._arr.push(item)
  }
  dequeue(){
    return this._arr.shift()
  }
}

const queue=new Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()//1


class Stack{
  constructor(){
    this._arr=[]
  }
  push(item){
    this._arr.push(item)
  }
  pop(){
    return this._arr.pop()
  }
  peek(){
    return this._arr[this._arr.length-1]
  }
}

const stack=new Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()

class Node {
  constructor(content,children=[]){
    this.content=content
    this.children=children
  }
}

const tree = new Node('hello',[
  new Node ('world'),
  new Node ('and'),
  new Node('fun',[
    new Node('javascript!')
  ])
])

function traverse(node){
  console.log(node.content)
  for (let child of node.children){
    traverse(child)
  }
}

traverse(tree)
// hello world and fun javascript