#include <stdio.h>
#include <stdlib.h>

struct node
{
    int a;
    struct node *next,*pre;
};

struct node* getnode()
{
    return((struct node *)malloc(sizeof(struct node)));
}

void inputnode(int *p)
{
    printf("enter a\n");
    fflush(stdin);
    scanf("%d",&*p);
    fflush(stdin);
}

struct node *createRLL()
{
    struct node *first,*nw,*prew;
    first=nw=prew=NULL;

    char c;
    do
    {
        prew=nw;
        nw=getnode();
        inputnode(&nw->a);
        if(first == NULL)
        {
            first=nw;
            nw->pre=NULL;//extra
        }
        else
        {
            prew->next=nw;
            nw->pre=prew;
        }
            printf("s for more nodes\n");
            fflush(stdin);
            scanf("%c",&c);
            fflush(stdin);
    }while(c=='s');

    nw->next=NULL;
    return(first);
}

struct node* createLLL()
{
    struct node *prew,*nw,*last;
    prew=nw=NULL;
    char c;

    do
    {
        prew=nw;
        nw=getnode();
        inputnode(&nw->a);

        if(prew==NULL)//to access last node
            last=nw;

        if(prew!=NULL)
            prew->pre=nw;

        nw->next=prew;


        printf("s for more nodes\n");
        fflush(stdin);
        scanf("%c",&c);
        fflush(stdin);
        nw->pre=NULL;

    }while(c=='s');
    return(nw);
}


void displayLL(struct node *p)
{
    for(;p!=NULL;p=p->next)
    {
        printf("%d\t",p->a);
    }
}


int main()
{
    struct node *first=NULL;
    int c;
    do
    {
        printf("\n\nEnter your choice\n1] create right sided linked list\n2] create left sided link list\n3] display linked list\n4] EXIT\n");
        scanf("%d",&c);
        fflush(stdin);
        switch (c)
        {
            case 1: first=createRLL();
                      break;

            case 2: first=createLLL();
                      break;

            case 3: displayLL(first);
                      break;

            case 4: break;

            default : printf("Enter right choice\n");
        }
    }while(c!=12);
    return 0;
}
