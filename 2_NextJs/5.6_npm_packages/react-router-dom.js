// ###### REACT-ROUTER-DOM - 4 STEPS

// ############################## - App.js
        import React from "react";
// 1/4 step - import parts        
        import { BrowserRouter, Routes, Route } from "react-router-dom"; 
        
        import Layout from './Layout';
        // ...

        function App() {
          return (
            <div className="App">
            
{/* 2/3 step - usage */}
              <BrowserRouter>
                <Routes>
                  <Route path="/" element={<Layout />}>
                      <Route index element={<Home />} />
                      <Route path="product/:id" element={<ProductView />} />
                      <Route path="prod-list/:page" element={<ProductsList />} />
                      <Route path="/contacts" element={<Contacts />} />
                      <Route path="*" element={<Empty />} />
                      </Route>
                  <Route path="/admin" element={<LayoutAdmin />}>
                      <Route index element={<AdminPanel />} />
                      <Route path="change-product/:id" element={<AdminChange />} />
                      <Route path="add-product" element={<AdminAdd />} />
                  </Route>
                </Routes>
              </BrowserRouter>
          </div>)};
        // ..


// ###################### - component.js

      import React from 'react';
// 3/4 step - import
      import { Outlet } from "react-router-dom";   

      import Header from "./components/Header";
      // ...

      export default function  Layout(){

          return ( <>
          <Preloader />
            <Header />
            <NavBar />
            <div className="container col-2">
              <Banner />
              <div className="row">
              <SiteBar />
{/* 4/4 step - Установить Outlet в то место где должна вывестись страница */}
              <Outlet /> 
              </div>
              </div>
          <Footer />
          <ModalBar />

          </>);
      }
