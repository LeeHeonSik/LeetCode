bool sameType(char p1, char p2) {
    if (p1 == '(' && p2 == ')')
        return true;
    else if (p1 == '{' && p2 == '}')
        return true;
    else if (p1 == '[' && p2 == ']')
        return true;
    else {return false;}
}


bool isValid(char * s){
    int c;
    c = strlen(s);
    if ((c % 2) == 1) {
        return false; 
    }
    
    char *stack = (char*)malloc((c + 1)*sizeof(char));
    int index=0, stackindex=0;
    
    while (s[index] != '\0') {
        if (stackindex != 0 && sameType(stack[stackindex-1],s[index])) {
            stack[--stackindex] = '\0';
        }
        else {
            stack[stackindex++] = s[index];
        }
        index++;
    }
    return (stackindex == 0) ? true : false;
}
//         else if (sameType(s[i], s[c-i-1])) {
//             equal = true;
//             c--;
//         }
//         else
//             return false;
//     }
//     return equal;
// }