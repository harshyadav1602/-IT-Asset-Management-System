const canvas =
document.getElementById("forgot-bg");


const scene =
new THREE.Scene();


scene.fog =
new THREE.Fog(
0x020617,
5,
20
);



const camera =
new THREE.PerspectiveCamera(
60,
window.innerWidth/window.innerHeight,
0.1,
1000
);



const renderer =
new THREE.WebGLRenderer({
canvas:canvas,
alpha:true
});


renderer.setSize(
window.innerWidth,
window.innerHeight
);



camera.position.z=5;



// Security Sphere

const geometry =
new THREE.IcosahedronGeometry(
1.2,
2
);



const material =
new THREE.MeshBasicMaterial({

color:0x00ffff,

wireframe:true

});



const shield =
new THREE.Mesh(
geometry,
material
);


scene.add(shield);



// Floating particles

let particles=[];


for(let i=0;i<120;i++)
{

let geo =
new THREE.SphereGeometry(
0.03,
8,
8
);


let mat =
new THREE.MeshBasicMaterial({

color:0x00ffff

});



let p =
new THREE.Mesh(
geo,
mat
);



p.position.x =
(Math.random()-0.5)*12;


p.position.y =
(Math.random()-0.5)*10;


p.position.z =
(Math.random()-0.5)*5;



scene.add(p);

particles.push(p);

}




function animate()
{

requestAnimationFrame(animate);



shield.rotation.x +=0.01;

shield.rotation.y +=0.015;



particles.forEach(p=>{

p.position.y +=0.003;


if(p.position.y>5)
{
p.position.y=-5;
}

});



renderer.render(
scene,
camera
);

}


animate();



window.addEventListener(
"resize",
()=>{


camera.aspect =
window.innerWidth/window.innerHeight;


camera.updateProjectionMatrix();


renderer.setSize(
window.innerWidth,
window.innerHeight
);


});