import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { GaleriaProductosComponent } from './components/galeria-productos/galeria-productos.component';
import { ProductoComponent } from './components/producto/producto.component';
import { LoginPageComponent } from './components/login-page/login-page.component';
import { LandingPageComponent } from './components/landing-page/landing-page.component';
import { RegistroComponent } from './components/registro/registro.component';
import { AcercaDeNosotrosComponent } from './components/acerca-de-nosotros/acerca-de-nosotros.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent, FooterComponent, GaleriaProductosComponent,LoginPageComponent, ProductoComponent, LandingPageComponent, RegistroComponent, AcercaDeNosotrosComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {

}
