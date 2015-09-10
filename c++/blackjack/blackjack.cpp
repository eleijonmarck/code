#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <string>

using namespace std;

     int card1;
     int card2;
     int card3;
     int card4;
     int cardtotal;
     string hitstick;
     
int main() {
    
    void dealCards();
    void dealThirdCard();
    void dealFourthCard();
    void dealerPlay();
    void youLose();
    void youWin();
    
    cout << "BlackJack" << endl;
    cout << "*********" << endl;
    cout << "Welcome to BlackJack!" << endl;
    cout << "Please press ENTER twice to draw your first 2 cards" << endl;
    cin.get();
    dealCards();
    cout << "Card 1: " << card1 << endl;
    cout << "Card 2: " << card2 << endl;
                       cardtotal = card1+card2;
    cout << endl;
    cout << "Your card total is: " << cardtotal << endl;
    cin.get();
                       if (cardtotal>21) {
                                         youLose();
                                         }
                       if (cardtotal==21)
                                         {
                                         youWin();          
                                         }
    cout << "Do you want to 'Hit' or 'Stick'" << endl;
    cin >> hitstick;
        if (hitstick=="Hit") {
                             dealThirdCard();
                             }
        if (hitstick=="Stick") {
                               dealerPlay();
                               }
    system("cls");
    cout << "BlackJack" << endl;
    cout << "*********" << endl;
    cout << endl;
    cout << "Card 1: " << card1 << endl;
    cout << "Card 2: " << card2 << endl;
    cout << "Card 3: " << card3 << endl;
    cout << endl;
         cardtotal = cardtotal + card3;
    cout << "Your cardtotal is: " << cardtotal << endl;
    cin.get();
                       if (cardtotal>21) {
                                         youLose();
                                         }
                       if (cardtotal==21) {
                                          youWin();
                                          }
    cout << "Do you want to 'Hit' or 'Stick'" << endl;
    cin >> hitstick;
        if (hitstick=="Hit") {
                             dealFourthCard();
                             }
        if (hitstick=="Stick") {
                               dealerPlay();
                               }
        system("cls");
        cout << "BlackJack" << endl;
        cout << "*********" << endl;
        cout << endl;
        cout << "Card 1: " << card1 << endl;
        cout << "Card 2: " << card2 << endl;
        cout << "Card 3: " << card3 << endl;
        cout << "Card 4: " << card4 << endl;
        cout << endl;
             cardtotal = cardtotal + card4;
        cout << "Your cardtotal is: " << cardtotal << endl;
        cin.get();
                           if (cardtotal>21) {
                                             youLose();
                                             }
                           if (cardtotal==21) {
                                              youWin();
                                              }      
    return 0;
    }
    
void dealCards() {

     srand(time(NULL));
     card1 = rand() % 11 + 1;
     card2 = rand() % 11 + 1;
     }

void dealThirdCard() {
     
     srand(time(NULL));
     card3 = rand() % 11 + 1;
     }
     
void dealFourthCard() {
     
     srand(time(NULL));
     card4 = rand() % 11 + 1;
     }

void dealerPlay() {
     return;
     }

void youLose() {
     system("cls");
     cout << "BlackJack" << endl;
     cout << "*********" << endl;
     cout << endl;
     cout << "Sorry, you have bust!" << endl;
     cin.ignore().get();
     return;
     }
     
void youWin() {
     system("cls");
     cout << "BlackJack" << endl;
     cout << "*********" << endl;
     cout << endl;
     cout << "Congratulations! You win!" << endl;
     cin.ignore().get();
     return;
     }
