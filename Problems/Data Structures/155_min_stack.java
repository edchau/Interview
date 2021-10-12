/**
 * Design a stack that supports push, pop, top, and retrieving 
 * the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

 */

class MinStack {

    private Node head;
    
    public MinStack() {
        // Nothing
    }
    
    public void push(int val) {
        // Stores new min value on head each time 
        // we insert, if popped off, min is previous value
        if (head == null) 
            head = new Node(val, val, null);
        else 
            head = new Node(val, Math.min(val, head.min), head);
    }
    
    public void pop() {
        head = head.next;
    }
    
    public int top() {
        return head.val;
    }
    
    public int getMin() {
        return head.min;
    }
    
    
    private class Node {
        int val;
        int min;
        Node next;
            
        private Node(int val, int min, Node next) {
            this.val = val;
            this.min = min;
            this.next = next;
        }
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */