#include <stdio.h>
#include <stdlib.h>


struct AdjListNode{
    int dest;
    struct AdjListNode* next;
};


struct AdjList{
    struct AdjListNode* head;
};


struct Graph{
    int V;  
    struct AdjList* array;
};

// Create the graph
struct Graph* createGraph(int V){

    struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph));
    graph->V = V;

    graph->array = (struct AdjList*) malloc(V * sizeof(struct AdjList));

    for(int i = 0; i < V; i++){
        graph->array[i].head = NULL;
    }

    return graph;
}


struct AdjListNode* newAdjListNode(int dest){
    
    struct AdjListNode* newNode = (struct AdjListNode*) malloc(sizeof(struct AdjListNode));
    
    newNode->dest = dest;
    newNode->next = NULL;

    return newNode;
}


void addEdge(struct Graph* graph, int src, int dest){

    struct AdjListNode* newNode = newAdjListNode(dest);
    newNode->next = graph->array[src].head;
    graph->array[src].head = newNode;

    newNode = newAdjListNode(src);
    newNode->next = graph->array[dest].head;
    graph->array[dest].head = newNode;

}


void deleteEdge(struct Graph* graph, int src, int dest){
    struct AdjListNode* temp = graph->array[src].head;
    struct AdjListNode* prev = NULL;

    while(temp != NULL && temp->dest != dest){
        prev = temp;
        temp = temp->next;
    }
    if(temp != NULL){
        if(prev != NULL)
            prev->next = temp->next;
        else
            graph->array[src].head = temp->next;
        free(temp);
    }


    temp = graph->array[dest].head;
    prev = NULL;
    while(temp != NULL && temp->dest != src){
        prev = temp;
        temp = temp->next;
    } 
    if(temp != NULL){
        if(prev != NULL)
            prev->next = temp->next;
        else
            graph->array[dest].head = temp->next;
        free(temp);
    }
}

int main(void){
    
    


    return 0;
}