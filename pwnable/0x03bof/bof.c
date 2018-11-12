#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
	char overflowme[32];
	printf("overflow me : ");
	gets(overflowme);	// smash me!
	if(key == 0x4e4e4e4e){
		printf("%i\n%i\n%i\n", key, 0xcafebabe, 0x4e4e4e4e);
		system("/bin/sh");
	}
	else{
		printf("%i\n%i\n%i\n", key, 0xcafebabe, 0x4e4e4e4e);
		printf("Nah..\n");
	}
}
int main(int argc, char* argv[]){
	func(0xdeadbeef);
	return 0;
}

