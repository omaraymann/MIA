#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct
{
    int index;
    char description[100];
    int complete; // 1 if the task is completed and 0 when it is not completed
} tasks;
tasks arr[100];
int tasks_cntr=0;
void load()  //loads the tasks from the file
{
    FILE*f1=fopen("task manager.txt","r");
    if(f1==NULL)
    {
        printf("Error Opening The File");
        exit(0);
    }
    while(!feof(f1))
    {
        fscanf(f1,"%d,%[^,],%d\n",&arr[tasks_cntr].index,arr[tasks_cntr].description,&arr[tasks_cntr].complete);
        tasks_cntr++;
    }
    fclose(f1);
}
void add_task()
{
    printf("Enter Task Description: ");
    gets(arr[tasks_cntr].description);
    printf("\n");
    arr[tasks_cntr].index=tasks_cntr+1;
    arr[tasks_cntr++].complete=0;
    menu();
}
void view_tasks()
{
    if(tasks_cntr==0)
        printf("No Tasks Available\n\n");
    else
    {
        for(int i=0; i<tasks_cntr; i++)
        {
            printf("Index: %d\n",arr[i].index);
            printf("Description: %s\n\n",arr[i].description);
        }
    }
    menu();
}
void remove_task()
{
    int input;
    printf("Enter Task Index: ");
    scanf("%d",&input);
    char c=getchar();
    printf("\n");
    if(input<1 || input>tasks_cntr)
    {
        printf("Task Not Found!\n\n");
    }
    else
    {
        for(int i=input; i<tasks_cntr; i++)
        {
            arr[i-1].complete=arr[i].complete;
            strcpy(arr[i-1].description,arr[i].description);
        }
        tasks_cntr--;
        printf("TASK REMOVED SUCCESSFULLY\n\n");
    }
}
void mark_complete()
{
    int input;
    printf("Enter Task Index: ");
    scanf("%d",&input);
    char c=getchar();
    printf("\n");
    if(input<1 || input>tasks_cntr)
    {
        printf("Task Not Found!\n\n");
    }
    else if(arr[input-1].complete==1)
        printf("Task Is Already Marked Complete\n\n");
    else
    {
        arr[input-1].complete=1;
        printf("Task successfully Marked complete\n\n");
    }
}
void view_complete_incomplete()
{
    if(tasks_cntr==0)
        printf("No Tasks Available");
    else
    {
        printf("________________\n\n COMPLETE TASKS:\n________________\n\n");
        for(int i=0; i<tasks_cntr; i++)
        {
            if(arr[i].complete==1)
            {
                printf(" Index: %d\n",arr[i].index);
                printf(" Description: %s\n\n",arr[i].description);
            }
        }
        printf("__________________\n\n INCOMPLETE TASKS:\n__________________\n\n");
        for(int i=0; i<tasks_cntr; i++)
        {
            if(arr[i].complete==0)
            {
                printf("Index: %d\n",arr[i].index);
                printf("Description: %s\n\n",arr[i].description);
            }

        }
    }
}
void save()
{
    FILE*f1=fopen("task manager.txt","w");
    for(int i=0;i<tasks_cntr;i++)
    {
        fprintf(f1,"%d,%s,%d\n",arr[i].index,arr[i].description,arr[i].complete);
    }
    fclose(f1);
}
void menu()
{
    char input[10];
    printf("Minions Task Manager\n 1. Add Task\n 2. View Task\n 3. Remove Task\n 4. Mark Task As Completed\n 5. View Complete And Incomplete Tasks \n 6. Exit\n\nSelect an option: ");
    gets(input);
    printf("\n");
    if(strcmp(input,"1")==0)
        add_task();
    else if(strcmp(input,"2")==0)
        view_tasks();
    else if(strcmp(input,"3")==0)
        remove_task();
    else if(strcmp(input,"4")==0)
        mark_complete();
    else if(strcmp(input,"5")==0)
        view_complete_incomplete();
    else if(strcmp(input,"6")==0)
    {
        save();
        exit(0);
    }
    else
    {
        printf("Invalid Input\n\n");
        menu();
    }
    menu();

}
int main()
{
    load();
    menu();
    return 0;
}
