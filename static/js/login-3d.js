const canvas = document.getElementById("bg-animation");


const scene = new THREE.Scene();


scene.fog = new THREE.Fog(
    0x020617,
    5,
    20
);



const camera = new THREE.PerspectiveCamera(
    60,
    window.innerWidth/window.innerHeight,
    0.1,
    1000
);



const renderer = new THREE.WebGLRenderer({
    canvas:canvas,
    alpha:true
});


renderer.setSize(
    window.innerWidth,
    window.innerHeight
);



camera.position.z = 6;



// =======================
// 3D NETWORK GRID
// =======================


const grid = new THREE.GridHelper(
    20,
    40,
    0x00ffff,
    0x003344
);


grid.rotation.x = Math.PI/2.5;

scene.add(grid);




// =======================
// GLOWING DATA NODES
// =======================


let nodes=[];


for(let i=0;i<80;i++)
{


    let geometry =
    new THREE.SphereGeometry(
        0.06,
        16,
        16
    );


    let material =
    new THREE.MeshBasicMaterial({

        color:0x00ffff

    });



    let node =
    new THREE.Mesh(
        geometry,
        material
    );


    node.position.x =
    (Math.random()-0.5)*12;


    node.position.y =
    (Math.random()-0.5)*8;


    node.position.z =
    (Math.random()-0.5)*5;



    scene.add(node);

    nodes.push(node);

}




// =======================
// ANIMATION
// =======================


function animate()
{

    requestAnimationFrame(animate);



    grid.position.z +=0.02;



    if(grid.position.z>1)
    {
        grid.position.z=0;
    }



    nodes.forEach(node=>{

        node.rotation.x +=0.02;

        node.position.y +=0.002;


        if(node.position.y>4)
        {
            node.position.y=-4;
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