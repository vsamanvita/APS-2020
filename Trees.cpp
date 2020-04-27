//Binary tree
//construction,traversal,deletion,search,leafnodes,mirror image etc.
#include <stdio.h>
#include <stdlib.h>

struct node
{
    int a;
    struct node *left,*right;
};

struct node* getnode()
{
    return((struct node*)malloc(sizeof(struct node)));
}

void readdata(int *p)
{
    printf("\n enter the data\n");
    scanf("%d",&*p);
}

struct node* insertnode(struct node *root)
{
    struct node *cur,*nw;
    nw=getnode();
    nw->left=nw->right=NULL;
    readdata(&nw->a);
    if(root==NULL)
        root=nw;
    else
    {
        cur=root;
        while(1)
        {

        if(nw->a > cur->a)
        {
            if(cur->right==NULL)
            {
               cur->right=nw;
               break;
            }
            else
                cur=cur->right;
        }

        else if(nw->a < cur->a)
        {
            if(cur->left==NULL)
            {
                cur->left=nw;
                break;
            }
            else
                cur=cur->left;
        }

        else
        {
            printf("\nalready node exists\n");
            break;
        }
        }
    }
    return(root);
}

void inorder(struct node *root)
{
    if(root==NULL)
        return;
    inorder(root->left);
    printf("%d\t",root->a);
    inorder(root->right);
}

void preorder(struct node *root)
{
    if(root==NULL)
        return;
    printf("%d\t",root->a);
    preorder(root->left);
    preorder(root->right);
}

void postorder(struct node *root)
{
    if(root==NULL)
        return;
    postorder(root->left);
    postorder(root->right);
    printf("%d\t",root->a);
}

int totalnodes(struct node *root)
{
    static int count=0;
    if(root==NULL)
        return 0;
    totalnodes(root->left);
    count++;
    totalnodes(root->right);
    return(count);
}


int parentnodes(struct node *root)
{
    static int count=0;
    if(root==NULL)
        return 0;
    parentnodes(root->left);
    if(root->left!=NULL || root->right!=NULL)
        count++;
    parentnodes(root->right);
    return(count);
}


int leafnodes(struct node *root)
{
    static int count=0;
    if(root==NULL)
        return 0;
    leafnodes(root->left);
    if(root->left==NULL && root->right==NULL)
        count++;
    leafnodes(root->right);
    return(count);
}


void mirrorimage(struct node *root)
{
    struct node *temp=NULL;
    if(root==NULL)
        return;

    mirrorimage(root->left);
    temp=root->left;
    root->left=root->right;
    root->right=temp;
    mirrorimage(root->right);
}


void searchnode(struct node *root)
{
    int n,key=0;
    printf("enter the data to be searched\n");
    scanf("%d",&n);
    while(root!=NULL)
    {
        if(n < root->a)
            root=root->left;
        else if(n > root->a)
            root=root->right;
        else
        {
            printf("key found\n");
            key=1;
            break;
        }
    }
    if(key==0)
        printf("node not present\n");
}


void findparent(struct node *root)
{
    int x=root->a;
    struct node *parent;
    int n,key=0;
    printf("enter child node\n");
    scanf("%d",&n);
    while(key==0 && root!=NULL)
    {
        if(n < root->a)
        {
             parent=root;
             root=root->left;
        }
        else if(n > root->a)
        {
            parent=root;
            root=root->right;
        }
        else
        {
            if(root->a==x)
                printf("root node\n");
            else
                printf("parent node : %d",parent->a);
            key=1;
        }
    }
    if(key==0)
        printf("node not present\n");
}

struct node* deletenode(struct node *root)
{
    int x=root->a;
    struct node *parent,*del,*cur;
    del=root;
    parent=NULL;
    int n,key=0;
    printf("enter the data to be deleted\n");
    scanf("%d",&n);
    while(key==0 && del!=NULL)
    {
        if(n < del->a)
        {
             parent=del;
             del=del->left;
        }
        else if(n > del->a)
        {
            parent=del;
            del=del->right;
        }
        else
        {
            key=1;
        }
    }
    if(key==0)
    {
        printf("node not present\n");
        return(root);
    }

    if(del->left!=NULL && del->right!=NULL)
    {
        for(cur=del->left;cur->right->right!=NULL;cur=cur->right);
            del->a=cur->right->a;

            if(cur->right->left!=NULL)
                cur->right=cur->right->left;
            else
                cur->right=NULL;
            free(cur->right);
    }

    else if(del->right!=NULL)
    {
        if(del==root)
            root=root->right;
        else if(del==parent->right)
            parent->right=del->right;
        else
            parent->left=del->right;
    }

    else if(del->left!=NULL)
    {
        if(del==root)
            root=root->left;
        else if(del==parent->right)
            parent->right=del->left;
        else
            parent->left=del->left;
    }

    else
    {
        if(del==root)
            root=NULL;
        else if(del==parent->right)
            parent->right=NULL;
        else
            parent->left=NULL;
    }
    return(root);
}

void findsibling(struct node *root)
{
    int x=root->a;
    struct node *parent;
    int n,key=0;
    printf("enter the node\n");
    scanf("%d",&n);
    if(n==x)
    {
       printf("it is root node\n");
       key=1;
    }
    while(key==0 && root!=NULL)
    {
        if(n < root->a)
        {
             parent=root;
             root=root->left;
        }
        else if(n > root->a)
        {
            parent=root;
            root=root->right;
        }
        else
        {
            if(parent->right==root)
                printf("sibling is:%d",parent->left->a);
            else
                printf("sibling is:%d",parent->right->a);
            key=1;
        }
    }
    if(key==0)
        printf("node not present\n");
}


int main()
{
    struct node *root=NULL;
    int ch,c;
    do
    {
        printf("\n1]insert\n2]inorder\n3]preorder\n4]postorder\n5]No of nodes\n6]No of leaf nodes\n7]No of parent nodes\n8]mirror image\n9]search node\n10]find parent\n11]delete node\n12]findsibling\n13]exit\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1: root=insertnode(root);
                    break;

            case 2: inorder(root);
                    break;

            case 3: preorder(root);
                    break;

            case 4: postorder(root);
                    break;

            case 5: c=totalnodes(root);
                    printf("no of nodes is:%d",c);
                    break;

            case 6: c=leafnodes(root);
                    printf("no of leafnodes is:%d",c);
                    break;

            case 7: c=parentnodes(root);
                    printf("no of non-leafnodes is:%d",c);
                    break;

            case 8: mirrorimage(root);
                    printf("Mirrored");
                    break;

            case 9: searchnode(root);
                    break;

            case 10:findparent(root);
                    break;

            case 11:root=deletenode(root);
                    break;

            case 12:findsibling(root);
                    break;

            case 13:break;

            default:printf("enter correct choice\n");
        }

    }while(ch!=13);
    return 0;
}