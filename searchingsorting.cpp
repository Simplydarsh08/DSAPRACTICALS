#include <iostream>
#include <cstring>
#include <ctime>
#include <cstdlib>
using namespace std;

// ---------------- Student Structure ----------------
struct Student {
    int ID;
    char Name[50];
    float CGPA;
};

// ---------------- Helper Functions ----------------

// Swap two student records
void swap(Student &a, Student &b) {
    Student temp = a;
    a = b;
    b = temp;
}

// Bubble Sort by Name (Alphabetical)
void bubbleSortByName(Student *arr, int n) {
    for(int i=0; i<n-1; i++)
        for(int j=0; j<n-i-1; j++)
            if(strcmp(arr[j].Name, arr[j+1].Name) > 0)
                swap(arr[j], arr[j+1]);
}

// Selection Sort by CGPA (Descending)
void selectionSortByCGPA(Student *arr, int n) {
    for(int i=0; i<n-1; i++){
        int max_idx = i;
        for(int j=i+1; j<n; j++)
            if(arr[j].CGPA > arr[max_idx].CGPA)
                max_idx = j;
        swap(arr[i], arr[max_idx]);
    }
}

// Linear Search by ID
int linearSearch(Student *arr, int n, int id) {
    for(int i=0; i<n; i++)
        if(arr[i].ID == id)
            return i; // found
    return -1; // not found
}

// Binary Search by ID (array must be sorted by ID)
int binarySearch(Student *arr, int n, int id) {
    int low = 0, high = n-1;
    while(low <= high) {
        int mid = (low + high) / 2;
        if(arr[mid].ID == id)
            return mid;
        else if(arr[mid].ID < id)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1; // not found
}

// Display student record
void displayStudent(Student s) {
    cout << "ID: " << s.ID << "\tName: " << s.Name << "\tCGPA: " << s.CGPA << endl;
}

// Display all students
void displayAll(Student *arr, int n) {
    for(int i=0; i<n; i++)
        displayStudent(arr[i]);
}

// ---------------- Main Program ----------------
int main() {
    Student *students = nullptr; // dynamically allocated array
    int n = 0; // current number of students
    int capacity = 2; // initial capacity

    students = (Student*)malloc(capacity * sizeof(Student));

    int choice;
    do {
        cout << "\n--- Student Database Menu ---\n";
        cout << "1. Add Student\n";
        cout << "2. Display All Students\n";
        cout << "3. Linear Search by ID\n";
        cout << "4. Binary Search by ID\n";
        cout << "5. Sort by Name (Bubble Sort)\n";
        cout << "6. Sort by CGPA Descending (Selection Sort)\n";
        cout << "7. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch(choice) {
            case 1: {
                // Expand array if needed
                if(n == capacity) {
                    capacity *= 2;
                    students = (Student*)realloc(students, capacity * sizeof(Student));
                }

                cout << "Enter ID: ";
                cin >> students[n].ID;
                cout << "Enter Name: ";
                cin.ignore(); // ignore newline
                cin.getline(students[n].Name, 50);
                cout << "Enter CGPA: ";
                cin >> students[n].CGPA;
                n++;
                break;
            }

            case 2:
                displayAll(students, n);
                break;

            case 3: {
                int id;
                cout << "Enter ID to search: ";
                cin >> id;
                int idx = linearSearch(students, n, id);
                if(idx!=-1) displayStudent(students[idx]);
                else cout << "Student not found.\n";
                break;
            }

            case 4: {
                int id;
                cout << "Enter ID to search: ";
                cin >> id;
                // Binary search requires sorting by ID first
                for(int i=0;i<n-1;i++)
                    for(int j=0;j<n-i-1;j++)
                        if(students[j].ID > students[j+1].ID)
                            swap(students[j], students[j+1]);
                int idx = binarySearch(students, n, id);
                if(idx!=-1) displayStudent(students[idx]);
                else cout << "Student not found.\n";
                break;
            }

            case 5:
                bubbleSortByName(students, n);
                cout << "Sorted by Name (Alphabetical).\n";
                break;

            case 6:
                selectionSortByCGPA(students, n);
                cout << "Sorted by CGPA (Descending).\n";
                break;

            case 7:
                cout << "Exiting...\n";
                break;

            default:
                cout << "Invalid choice.\n";
        }

    } while(choice != 7);

    free(students); // free dynamic memory
    return 0;
}


