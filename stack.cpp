#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Node structure for linked list
struct Node {
    char data;
    Node* next;
};

// Stack ADT using singly linked list
class Stack {
    Node* top;
public:
    Stack() { top = NULL; }

    bool isEmpty() {
        return top == NULL;
    }

    void push(char x) {
        Node* temp = new Node;
        temp->data = x;
        temp->next = top;
        top = temp;
    }

    char pop() {
        if (isEmpty()) return '\0';
        Node* temp = top;
        char x = temp->data;
        top = top->next;
        delete temp;
        return x;
    }

    char peek() {
        if (isEmpty()) return '\0';
        return top->data;
    }
};

// Function to return precedence of operators
int precedence(char ch) {
    if (ch == '+' || ch == '-') return 1;
    if (ch == '*' || ch == '/') return 2;
    if (ch == '^') return 3;
    return 0;
}

// Function to check if character is operator
bool isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^');
}

// Infix to Postfix conversion
string infixToPostfix(string infix) {
    Stack s;
    string postfix = "";
    for (char ch : infix) {
        if (isalnum(ch))
            postfix += ch;
        else if (ch == '(')
            s.push(ch);
        else if (ch == ')') {
            while (!s.isEmpty() && s.peek() != '(')
                postfix += s.pop();
            s.pop(); // remove '('
        } else {
            while (!s.isEmpty() && precedence(s.peek()) >= precedence(ch))
                postfix += s.pop();
            s.push(ch);
        }
    }
    while (!s.isEmpty())
        postfix += s.pop();
    return postfix;
}

// Infix to Prefix conversion
string infixToPrefix(string infix) {
    reverse(infix.begin(), infix.end());
    for (char &ch : infix) {
        if (ch == '(') ch = ')';
        else if (ch == ')') ch = '(';
    }
    string prefix = infixToPostfix(infix);
    reverse(prefix.begin(), prefix.end());
    return prefix;
}

// Main function
int main() {
    string infix;
    cout << "Enter infix expression: ";
    cin >> infix;

    cout << "Postfix Expression: " << infixToPostfix(infix) << endl;
    cout << "Prefix Expression: " << infixToPrefix(infix) << endl;

    return 0;
}


