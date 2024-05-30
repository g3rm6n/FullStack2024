import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ProductsService, Product } from '../../../services/products.service';
import { RouterModule } from '@angular/router';



@Component({
  selector: 'app-ingresar-productos',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterModule],
  templateUrl: './ingresar-productos.component.html',
  styleUrl: './ingresar-productos.component.css'
})
export class IngresarProductosComponent implements OnInit {

  productos: any[] = [];
  productoForm!: FormGroup;


  constructor(private producstService: ProductsService, private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.obtenerProductos();
    this.productoForm = this.formBuilder.group({
      modelo: ['', Validators.required],
      precio: ['', Validators.required],
      stock: ['', Validators.required],
      imagen: ['', Validators.required],
      detalle: [''],
      marca: ['', Validators.required],
      rodado: ['', Validators.required],
      estilo: ['', Validators.required],
      material: ['', Validators.required],
      color: ['', Validators.required]
    });
  }

  obtenerProductos(): void {
    this.producstService.getProducts().subscribe(
      data => {
        this.productos = data;
      },
      error => {
        console.error(error);
      }
    );
  }

  crearProducto(event:Event): void {
    event.preventDefault();
   
    if (this.productoForm.valid) {
      if (this.productoForm.valid) {
        const nuevoProducto: Product = {
          modelo: this.productoForm.value.modelo,
          precio: this.productoForm.value.precio,
          stock: this.productoForm.value.stock,
          imagen: this.productoForm.value.imagen,
          detalle: this.productoForm.value.detalle,
          marca: this.productoForm.value.marca,
          rodado: this.productoForm.value.rodado,
          estilo: this.productoForm.value.estilo,
          material: this.productoForm.value.material,
          color: this.productoForm.value.color,
        };
   
      console.log("Enviando al servidor...", nuevoProducto);

      this.producstService.postProducts(nuevoProducto).subscribe(
        data => {
          console.log("Producto creado:", data);
          this.obtenerProductos(); 
          this.productoForm.reset(); 
        },
        error => {
          console.error(error);
          
        }
      );
    } else {
      
      this.productoForm.markAllAsTouched();
    }
  }
  
}}