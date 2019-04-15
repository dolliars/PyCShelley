#include<stdio.h>
#include<stdlib.h>

int main()
{
	char *line = NULL;
	size_t len = 0;
	ssize_t nread;

	for(;;) {
		printf("$$ ");
		fflush(stdout);
		
		nread = getline(&line, &len, stdin); 

		printf("%s", line);
		if ( nread < 0) exit(0);
	}
}
