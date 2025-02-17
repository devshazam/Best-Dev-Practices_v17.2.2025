UxBYWpaWUqQvDrDREa

Hydration.js
'use client'
import * as React from 'react';
import UseStore from './(store)/store';

export default function Hydration() {
    React.useEffect(()=>{
        try{
            UseStore.persist.rehydrate();
        } catch(e){
            console.error('error in hrdration',e);
        }
    },[])

    return null;
}