#include <iostream>
using namespace std;

// Forward declaration of the class
class Student;

// Function prototype (with class scope)
void display(Student&);

// Class definition
class Student {
public:
    string name;
    int age;

    // Friend function declaration
    friend void display(Student&);
};

// Function definition
void display(Student& s) {
    cout << "Name: " << s.name << endl;
    cout << "Age: " << s.age << endl;
}

int main() {
    Student s1;
    s1.name = "Alice";
    s1.age = 20;

    // Call display function
    display(s1);

    return 0;
}

