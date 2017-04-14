/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package vectorscalarcarpim;

import java.util.ArrayList;

/**
 *
 * @author BM
 */
public class VectorScalarCarpim {

    /**
     * @param args the command line arguments
     */
    static int toplam = 0;
    public static int a[] = {1,2,3};
    public static int b[] = {2,4,6};
    public static int c[] = {2,3,6};
    public static void main(String[] args) {
        for (int i = 0; i < a.length; i++) {
            
            c[i] = a[i]*b[i];
            toplam = c[i] + toplam;
               
        }
        
       
        System.out.println(toplam);
    }
    
}
