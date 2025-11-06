3 - 
#include<iostream>
using namespace std;
#define SIZE 5 // Size can be changed from here
class CQueue
{
		int cque[5];
		int front, rear;

	public:
		CQueue()
		{
			front = rear = -1;
		}
		bool isEmpty()
		{
			return front == -1;
		}
		bool isFull()
		{
			return rear == SIZE - 1 && front == 0 || rear == front - 1;
		}
		void enque(int e)
		{
			if(!isFull())
			{
				if(front == -1) //for first element only
					front = 0;
				rear = (rear + 1) % SIZE;
				cque[rear] = e;
			}
			else
				std::cout << "Queue is Full" << "\n";
		}		
		int deque()
		{
			if(!isEmpty())
			{
				int temp = cque[front];
				front = (front + 1) % SIZE;

				if(front == (rear + 1) % SIZE) //Queue has become Empty
				{
					front = rear = -1;
				}
				
				return temp;
			}
			return -1;
		}

		void showQ()
		{
			cout << "Elements in Queue : ";
			for(int i = front; i != rear; i = (i + 1) % SIZE)
				cout << cque[i] << " ";
			cout << cque[rear];
			cout << endl;
		}
};
int main()
{
	CQueue cq;
	int choice,e;
	do
	{
		cout << "\n-----------MENU-----------\n";
		cout << "1. Enque\n";
		cout << "2. Deque\n";
		cout << "3. Display\n";
		cout << "4. Exit\n";
		cout << "Enter your choice : ";
		cin >> choice;
		cout << endl;

		switch(choice)
		{
			case 1:
				cout << "Enter element to be inserted : ";
				cin >> e;
				cq.enque(e);
				break;
			case 2:
				e = cq.deque();
				if(e != -1)
					cout << e << " Deleted from the queue.\n";
				else
					cout << "Queue is Empty!\n";
				break;
			case 3:
				cq.showQ();
				break;
			case 4:
				break;

			default:
				cout << "Wrong choice Entered!";
		}
	}while(choice != 4);


	return 0;
}

