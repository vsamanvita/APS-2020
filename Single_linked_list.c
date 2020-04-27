#include <stdio.h>
#include <stdlib.h>

struct node
{
    int a;
    struct node *next;
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
            first=nw;
        else
            prew->next=nw;

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
    struct node *prew,*nw;
    prew=nw=NULL;
    char c;

    do
    {
        prew=nw;
        nw=getnode();
        inputnode(&nw->a);

        nw->next=prew;

        printf("s for more nodes\n");
        fflush(stdin);
        scanf("%c",&c);
        fflush(stdin);

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

struct node* insertF(struct node *first)
{
    struct node *nw;
    char c;
    do
    {
        first=nw;
        nw=getnode();
        inputnode(&nw->a);
        nw->next=first;

        printf("s for more nodes\n");
        fflush(stdin);
        scanf("%c",&c);
        fflush(stdin);
    }while(c=='s');
    return (nw);
}

struct node* insertL(struct node *first)
{
    struct node *last,*nw;
    nw=getnode();
    inputnode(&nw->a);
    if(first==NULL)
    {
        first=nw;
        first->next=NULL;
    }
    else
    {
        for(last=first;last->next!=NULL;last=last->next);
        last->next=nw;
        nw->next=NULL;
    }
    return(first);
}

struct node* insertA(struct node *first)
{
    int n,z=1;
    printf("enter position\n");
    scanf("%d",&n);
    struct node *prew,*nex,*nw;
    nw=getnode();
    inputnode(&nw->a);
    if(first==NULL||z==1)
    {
        nw->next=first;
        return(nw);
    }
    else
    {
        for(prew=first;z<n;prew=prew->next,z++);
        {
            nex=prew->next;
            prew->next=nw;
            nw->next=nex;
        }
    }
    return(first);
}



struct node* deleteF(struct node *first)
{
    first=first->next;
    return(first);
}



struct node* deleteL(struct node *first)
{
    struct node *last,*prew;
    for(last=first,prew=NULL;last->next!=NULL;prew=last,last=last->next);
    {
        free(last);
        prew->next=NULL;
    }
    return(first);
}


struct node* deleteA(struct node *first)
{
    if(first==NULL)
        printf("no node present\n");
    else
    {
        int n;
        printf("enter the data to be deleted\n");
        scanf("%d",&n);
        struct node *prew,*del;
        for(del=first,prew=NULL;del->a!=n;prew=del,del=del->next);
            {
                if(del==NULL)
                    printf("data not present\n");
                else if(del==first)
                    first=first->next;
                else
                   prew->next=del->next;
            }
            free(del);
    }
    return(first);
}


struct node* sort(struct node *first)
{
    int z;
    struct node *i,*j;
    for(i=first;i->next!=NULL;i=i->next)
    {
        for(j=first;j->next!=NULL;j=j->next)
        {
            if(j->a>j->next->a)
            {
                z=j->a;
                j->a=j->next->a;
                j->next->a=z;
            }
        }
    }
    return(first);
}



struct node* reverse(struct node *first)
{
    if(first->next!=NULL)
    {
    struct node *i,*j,*k;
    i=first;
    j=i->next;
    k=j->next;
    while(j!=NULL)
    {
        j->next=i;
        i=j;
        j=k;
        if(k!=NULL)
            k=k->next;
    }

    first->next=NULL;
    first=i;
    }
    return(first);
}

int main()
{
    struct node *first=NULL;
    int c;
    do
    {
        printf("\n\nEnter your choice\n1] create right sided linked list\n2] create left sided link list\n3] display linked list\n4] insert at front\n5] insert at the end\n6] insert at any position\n7] delete first\n8] delete last\n9] delete at any position\n10] Sort\n11] reverse the link\n12] EXIT\n");
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

            case 4: first=insertF(first);
                      break;

            case 5: first=insertL(first);
                      break;

            case 6: first=insertA(first);
                      break;

            case 7: first=deleteF(first);
                      break;

            case 8: first=deleteL(first);
                      break;

            case 9: first=deleteA(first);
                      break;

            case 10: first=sort(first);
                       break;

            case 11: first=reverse(first);
                     break;

            case 12: break;

            default : printf("Enter right choice\n");
        }
    }while(c!=12);
    return 0;
}
