#include <iostream>
using namespace std;

int main() {
    int amount = 20000, deposit = 0, withdraw = 0, choice;
    int pin;

    cout << "Enter your PIN: ";
    cin >> pin;

    if (pin == 1998) {  
        cout << "\nPIN Approved!\n";
        cout << "===========================\n";
        cout << "\tWelcome to ATM\n";
        cout << "===========================\n";
        cout << "1. Check Balance\n";
        cout << "2. Withdraw\n";
        cout << "3. Deposit\n";
        cout << "4. Exit\n";
        cout << "===========================\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "\nYour current balance is: " << amount << "\n";
        } 
        else if (choice == 2) {
            cout << "\nEnter the amount you want to withdraw: ";
            cin >> withdraw;
            if (withdraw > amount) {
                cout << "\nYou do not have sufficient balance.\n";
            } else {
                amount -= withdraw;
                cout << "\nWithdrawal successful! Your new balance is: " << amount << "\n";
            }
        } 
        else if (choice == 3) {
            cout << "\nEnter the amount you want to deposit: ";
            cin >> deposit;
            amount += deposit;
            cout << "\nDeposit successful! Your new balance is: " << amount << "\n";
        } 
        else if (choice == 4) {
            cout << "\nThank you for using our ATM!\n";
        } 
        else {
            cout << "\nInvalid choice! Please enter 1-4.\n";
        }
    } 
    else {
        cout << "\nInvalid PIN! Please try again.\n";
    }

    return 0;
}