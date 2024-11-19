#include <stdio.h>
#include <string.h>
char string[10], action[10], stack[20], act[20];

int j = 0;

int main(){

    printf("Enter the string: ");
    scanf("%s", string);
    int string_length = strlen(string);
    strcpy(action, "SHIFT");
    printf("\nStack\tInput\tAction\n");
    for(int i=0, j=0;i<string_length;i++, j++){
        if(string[j] == 'i' && string[j] == 'd'){
            stack[i] = 'i';
            stack[i+1] = 'd';
            stack[i+2] = '\0';
            string[i] = ' ';
            string[i+1] = ' ';
            printf("\n%s\t%s\t%s",stack, string, action);
            check();
        }
        else{
            stack[i] = string[i];
            stack[i+1] = '\0';
            string[i] = ' ';
            printf("\n%s\t%s\t%s",stack, string, action);
            check();
        }
    }
    return 0;
}

void check(){
    for(int i=0;i<strlen(stack);i++){

    }
}