const canvas = document.getElementById("bg-animation");

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(
    60,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);

camera.position.z = 6;

const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    alpha: true,
    antialias: true
});

renderer.setSize(
    window.innerWidth,
    window.innerHeight
);

renderer.setPixelRatio(window.devicePixelRatio);

// =====================================
// FLOATING PARTICLES
// =====================================

const particleCount = 180;

const positions = [];

for (let i = 0; i < particleCount; i++) {

    positions.push(
        (Math.random() - 0.5) * 18,
        (Math.random() - 0.5) * 10,
        (Math.random() - 0.5) * 8
    );

}

const particleGeometry = new THREE.BufferGeometry();

particleGeometry.setAttribute(
    "position",
    new THREE.Float32BufferAttribute(
        positions,
        3
    )
);

const particleMaterial = new THREE.PointsMaterial({

    color: 0x00ffff,

    size: 0.08,

    transparent: true,

    opacity: 0.9

});

const particles = new THREE.Points(
    particleGeometry,
    particleMaterial
);

scene.add(particles);

// =====================================
// GLOWING ORBS
// =====================================

const orbs = [];

for (let i = 0; i < 12; i++) {

    const geometry = new THREE.SphereGeometry(
        0.18,
        24,
        24
    );

    const material = new THREE.MeshBasicMaterial({

        color: 0x00d4ff,

        transparent: true,

        opacity: 0.6

    });

    const orb = new THREE.Mesh(
        geometry,
        material
    );

    orb.position.set(

        (Math.random() - 0.5) * 14,

        (Math.random() - 0.5) * 8,

        (Math.random() - 0.5) * 4

    );

    orb.userData.speed =

        0.002 + Math.random() * 0.003;

    scene.add(orb);

    orbs.push(orb);

}

// =====================================
// AMBIENT LIGHT
// =====================================

const ambient = new THREE.AmbientLight(
    0xffffff,
    1
);

scene.add(ambient);

// =====================================
// ANIMATION
// =====================================

function animate() {

    requestAnimationFrame(animate);

    particles.rotation.y += 0.0008;

    particles.rotation.x += 0.0003;

    orbs.forEach((orb) => {

        orb.position.y += orb.userData.speed;

        orb.rotation.x += 0.01;

        orb.rotation.y += 0.01;

        if (orb.position.y > 5) {

            orb.position.y = -5;

        }

    });

    renderer.render(
        scene,
        camera
    );

}

animate();

// =====================================
// RESPONSIVE
// =====================================

window.addEventListener("resize", () => {

    camera.aspect =
        window.innerWidth / window.innerHeight;

    camera.updateProjectionMatrix();

    renderer.setSize(
        window.innerWidth,
        window.innerHeight
    );

});