#include <stdio.h>

int main()
{
  int c;

  printf("Enter any characters, `X' to exit\n");
  do {
    c = getchar();
    putchar(c);
  } while (c != 'X');

  return 0;
}
