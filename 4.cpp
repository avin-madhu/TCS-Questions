//sort a stack using recursion
#include <iostream>
#include <ostream>
#include <stack>
using namespace std;

void print_stack(stack<int> &st)
{
   stack<int> temp = st;
   while(!temp.empty())
   {
     cout<<temp.top()<<" ";
     temp.pop();
   }
   cout<<endl;
}

void sorted_insert(stack<int> &st, int num)
{
   if(st.empty() || st.top() > num)
   {
    st.push(num);
    return;
   }

   int temp = st.top();
   st.pop();
   sorted_insert(st,num);
   st.push(temp);
}


void sort_stack(stack<int> &st)
{
   if(st.empty())
   {
    return;
   }

   int temp = st.top();
   st.pop();
   sort_stack(st);
   sorted_insert(st,temp);

}

int main()
{
    stack<int> st;

    st.push(10);
    st.push(3);
    st.push(20);
    st.push(70);
    st.push(1);
    st.push(60);

    // the stack before
    cout<<"The stack before sorting: ";
    print_stack(st);  // No need to pass the size of the stack

    // Sort the stack
    sort_stack(st);  // No need to pass the size of the stack

    cout<<"The stack after sorting: ";
    print_stack(st);  // No need to pass the size of the stack
    
    return 0;
}
