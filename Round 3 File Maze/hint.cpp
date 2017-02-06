#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
int main()
{
	std::ofstream myfile;
 	int count = 1;
    	std::string ak;	
	std::cout<<"\n Your Question: ";						//your question goes here
	std::cin>>ak;
	if(ak=="answer" || ak=="Answer" || ak=="ANSWER")			//if correct answer entered display hint
	{	std::cout<<"\nGo to /bin/ for next hint\nUse cd /bin/ \n";
		myfile.open ("score.txt");					//initial clear : blank file include only in 1st hint
		myfile.close();
        	myfile.open ("score.txt",std::ios_base::app);
        	myfile << "\nCleared Hint 1 Score: 1\n";
        	myfile.close();
		system("rm hint*");						//remove hint 
    	}
	else
	{	std::cout<<"\nWrong answer execute binary again and enter correct answer\n";
		system("./hint");
		count++;

	}
	myfile.open ("score.txt",std::ios_base::app);
        myfile << "\nAttempts for Hint 1: "<<count;
        myfile.close();
	return 0;
}

