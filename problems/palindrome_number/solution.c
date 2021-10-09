

bool isPalindrome(int x){
    int i;
    if (x < 0) {
        return false;
    }
    else if (x == 0) {
        return true;
    }
    long long s, k;
    s = 0;
    k = x;
    while (x != 0) {
        s *= 10;
        s += x %  10;
        x /= 10;
    }
    if (k == s) {
        return true;
    }
    else return false;
}