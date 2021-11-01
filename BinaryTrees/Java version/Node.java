import java.util.*;
import java.util.Scanner;

import javax.print.event.PrintEvent;

public class Node{
    public int data;
    Node leftNode;
    Node rightNode;

    public Node(){}
    
    void display(){
        System.out.println(data);
    }
}

class Tree extends Node{
    private Node root;

    public Tree(){
        root = null;
    }
    public Node search(int data){
        Node current = root;
        System.out.println("elements:");
        while(current.data != data){
            if(current != null)
            System.out.println(current.data+" ");
            if(current.data>data)
                current = current.leftNode;
            else{
                current = current.rightNode;
            }
            if(current == null)
            return null;
        }
        return current;
    }
    public Node insert(int data){
        Node temp = new Node();
        temp.data = data;
        if(root == null){
        root = temp;
        }
        else{
            Node current = root;
            Node parent = null;
            while(true){
                parent = current;
                if(data<parent.data){
                    current = current.leftNode;
                    if (current == null){
                        parent.leftNode = temp;
                        return parent;
                    }
                }
                else{
                    current = current.rightNode;
                    if(current==null){
                        parent.rightNode = temp ;
                        return parent;
                    }
                }
            }
        }
        return null;
    }
    public Node preorder(Node root){
        if(root!=null)
        System.out.println(root.data+" ");
        preorder(root.leftNode);
        preorder(root.rightNode);
        return null;
    }
    public Node inorder(Node root){
        if(root!=null)
        inorder(root.leftNode);
        System.out.println(root.data+" ");
        inorder(root.rightNode);
        return null;
    }
    public Node postorder(Node root){
        if(root!=null)
        postorder(root.leftNode);
        postorder(root.rightNode);
        System.out.println(root.data+" ");
        return null;
    }
    public void traverse(int traverseval){
        switch(traverseval){
            case 1 : System.out.println("preorder");
                        preorder(root);
                        break;
            case 2 : System.out.println("inorder");
                    inorder(root);
                    break;
            case 3 : System.out.println("postorder");
                    postorder(root);
                    break;
            default: System.out.println("Wrong input please, chose from options 1,2 and 3");

        }
    }
}