#include <iostream>

using namespace std;
/*
int main() {

    int c = 0;

    while (c != 1000) {

        c += 1;
        cout << c << endl;

    }

    return 0;
}
*/

void hello();

int main() {

    for (int c = 0; c <= 1000; c++) {

        cout << "TESTE" << " " << c << endl;
        hello();

    }

    return 0;
}

void hello() {

    cout << "Hello World!" << endl;

}
