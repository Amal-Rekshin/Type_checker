#include <stdio.h>
#include <string.h>

typedef struct {
    char name[20];
    char type[10];
} Symbol;

Symbol symbolTable[20];
int symbolCount = 0;
void addVariable(const char *name, const char *type) {
int i;
    for (i = 0; i < symbolCount; i++) {
	if (strcmp(symbolTable[i].name, name) == 0) {
		printf("Error: Variable '%s' already declared.\n", name);
		return;
	}
    }
    strcpy(symbolTable[symbolCount].name, name);
    strcpy(symbolTable[symbolCount].type, type);
    symbolCount++;
}
const char *getType(const char *name) {
int i;
    for (i = 0; i < symbolCount; i++) {
	if (strcmp(symbolTable[i].name, name) == 0) {
		return symbolTable[i].type;
	}
    }
    return NULL;
}
void processInput(const char *input) {
    char var1[20], var2[20], type[10];
    if (sscanf(input, "declare %s %s", var1, type) == 2) {
	addVariable(var1, type);
    } else if (sscanf(input, "%s = %s", var1, var2) == 2) {
	const char *type1 = getType(var1);
	const char *type2 = getType(var2);
	if (!type1) {
	    printf("Error: Variable '%s' not declared.\n", var1);
	} else if (type2 && strcmp(type1, type2) != 0) {
	    printf("Error: Type mismatch between '%s' and '%s'.\n", var1, var2);
	} else if (!type2 && strcmp(type1, "int") == 0 && strchr(var2, '.') != NULL) {
	    printf("Error: Cannot assign float to int variable '%s'.\n", var1);
	} else {
	    printf("Assignment '%s = %s' is valid.\n", var1, var2);
	}
    } else {
	printf("Error: Invalid statement.\n");
    }
}

int main() {
    char input[50];
    printf("Simple Type Checker\nType 'exit' to quit.\n");

    while (1) {
	printf("> ");
	fgets(input, sizeof(input), stdin);
	input[strcspn(input, "\n")] = 0;
	if (strcmp(input, "exit") == 0) break;
	processInput(input);
    }

    printf("Exiting program.\n");
    return 0;
}
