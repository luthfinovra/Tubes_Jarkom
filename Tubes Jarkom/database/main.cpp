#include "SLL.h"
int main()
{
    element a;
    List L;
    L.first = NULL;
    adr p, temp, j;
    int n;
    cout << "Masukkan angka positif: (exit input -1)!" << endl;
    cin >> n;
    while(n != -1){
        p = newelement(n);
        cout << p << endl;
        if(L.first == NULL){
            L.first = p;
            temp = p;
            j = temp;
        }else{
            j -> next = p;
            temp = j->next;
            j = temp;
        }
        cout << "Masukkan angka positif: (exit input -1)!" << endl;
        cin >> n;
    }
    adr i = L.first;
    while(i != NULL){
        a = *i;
        cout << a.info << " ";
        i = a.next;
        cout << i << " " << endl;
    }
    return 0;
}
