#include <iostream>
#include <vector>

using namespace std;

// Define a Student class to store student records
class Student {
public:
    string name;
    int rollNo;
    double grade;

    Student(string n, int r, double g) {
        name = n;
        rollNo = r;
        grade = g;
    }
};

// Function to display the menu
void displayMenu() {
    cout << "Student Record Management System" << endl;
    cout << "1. Add Student" << endl;
    cout << "2. View Students" << endl;
    cout << "3. Update Student" << endl;
    cout << "4. Delete Student" << endl;
    cout << "5. Quit" << endl;
    cout << "Enter your choice: ";
}

// Function to add a new student record
void addStudent(vector<Student>& students) {
    string name;
    int rollNo;
    double grade;

    cout << "Enter student name: ";
    cin >> name;
    cout << "Enter student roll number: ";
    cin >> rollNo;
    cout << "Enter student grade: ";
    cin >> grade;

    students.push_back(Student(name, rollNo, grade));
    cout << "Student added successfully!" << endl;
}

// Function to view all student records
void viewStudents(const vector<Student>& students) {
    if (students.empty()) {
        cout << "No student records available." << endl;
    } else {
        cout << "Student Records:" << endl;
        for (const Student& student : students) {
            cout << "Name: " << student.name << ", Roll No: " << student.rollNo << ", Grade: " << student.grade << endl;
        }
    }
}

// Function to update a student record
void updateStudent(vector<Student>& students) {
    int rollNo;
    double newGrade;

    cout << "Enter student roll number to update: ";
    cin >> rollNo;

    for (Student& student : students) {
        if (student.rollNo == rollNo) {
            cout << "Enter new grade: ";
            cin >> newGrade;
            student.grade = newGrade;
            cout << "Student record updated successfully!" << endl;
            return;
        }
    }

    cout << "Student with roll number " << rollNo << " not found." << endl;
}

// Function to delete a student record
void deleteStudent(vector<Student>& students) {
    int rollNo;

    cout << "Enter student roll number to delete: ";
    cin >> rollNo;

    for (auto it = students.begin(); it != students.end(); ++it) {
        if (it->rollNo == rollNo) {
            it = students.erase(it);
            cout << "Student record deleted successfully!" << endl;
            return;
        }
    }

    cout << "Student with roll number " << rollNo << " not found." << endl;
}

int main() {
    vector<Student> students;
    int choice;

    do {
        displayMenu();
        cin >> choice;

        switch (choice) {
            case 1:
                addStudent(students);
                break;
            case 2:
                viewStudents(students);
                break;
            case 3:
                updateStudent(students);
                break;
            case 4:
                deleteStudent(students);
                break;
            case 5:
                cout << "Goodbye!" << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 5);

    return 0;
}
