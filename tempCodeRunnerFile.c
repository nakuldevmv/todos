#include <stdio.h>
#include <ctype.h>

char stack[100][3]; int top = -1, t = 1;
void push(char *s) { sprintf(stack[++top], "%s", s); }
char* pop() { return stack[top--]; }

void generateCode(char *postfix) {
    for (int i = 0; postfix[i]; i++) {
        if (isalnum(postfix[i])) {
            char op[2] = {postfix[i], '\0'}; push(op);
        } else {
            printf("LOAD %s\n%s %s\nSTORE T%d\n", stack[top-1], 
                   postfix[i] == '+' ? "ADD" : postfix[i] == '-' ? "SUB" :
                   postfix[i] == '*' ? "MUL" : "DIV", stack[top], t);
            sprintf(stack[--top], "T%d", t++);
        }
    }
}

int main() {
    char postfix[100];
    printf("Enter postfix: "); scanf("%s", postfix);
    generateCode(postfix);
}
