


int climbStairs(int n){
    if ( n == 1 ) {
        return 1;
    }
    if ( n == 2 ) {
        return 2;
    }
    int i, prev, current, temp; 
    prev = 1;
    current = 2;
    for ( i = 3; i <= n; i++ ) {
        temp = prev + current;
        prev = current;
        current = temp;
    }
    return current;
}