import {OrbitControls} from 'https://unpkg.com/three@0.127.0/examples/jsm/controls/OrbitControls.js'
import * as THREE from 'https://unpkg.com/three@0.127.0/build/three.module.js';


const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const light1 = new THREE.DirectionalLight(0xffffff, 3);
light1.position.set(1, 1, 1).normalize();
scene.add(light1);
const light2 = new THREE.DirectionalLight(0xffffff, 3);
light2.position.set(-1, -1, -1).normalize();
scene.add(light2);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
renderer.setClearColor(0xbfe3dd);
function check_exist(i, j, k) {
    if(i==1 && j==1 && k==1){
        return false
    }
    if ((0 <= i && i <= 2) && (0 <= j && j <= 2) && (0 <= k && k <= 2)) {
        return true
    }
    else {
        return false
    }
}
function check_3d_cube(cube_3d, turn) {
    console.log(cube_3d);
    var exists = [];
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            for (let k = 0; k < 3; k++) {
                if (cube_3d[i][j][k] == turn) {
                    if (check_exist(i + 1, j, k)) {
                        if (cube_3d[i + 1][j][k] == turn) {
                            if (check_exist(i + 2, j, k)) {
                                if (cube_3d[i + 2][j][k] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([(i + 2), j, k])
                                }
                            }
                        }
                    }
                    if (check_exist(i, j + 1, k)) {
                        if (cube_3d[i][j + 1][k] == turn) {
                            if (check_exist(i, j + 2, k)) {
                                if (cube_3d[i][j + 2][k] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([i, (j + 2), k])
                                }
                            }
                        }
                    }
                    if (check_exist(i, j, k + 1)) {
                        if (cube_3d[i][j][k + 1] == turn) {
                            if (check_exist(i, j, k + 2)) {
                                if (cube_3d[i][j][k + 2] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([i, j, (k + 2)])
                                }
                            }
                        }
                    }
                    if (check_exist(i + 1, j + 1, k)) {
                        if (cube_3d[i + 1][j + 1][k] == turn) {
                            if (check_exist(i + 2, j + 2, k)) {
                                if (cube_3d[i + 2][j + 2][k] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([(i + 2), (j + 2), k])
                                }
                            }
                        }
                    }
                    if (check_exist(i + 1, j, k + 1)) {
                        if (cube_3d[i + 1][j][k + 1] == turn) {
                            if (check_exist(i + 2, j, k + 2)) {
                                if (cube_3d[i + 2][j][k + 2] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([(i + 2), j, (k + 2)])
                                }
                            }
                        }
                    }
                    if (check_exist(i, j + 1, k + 1)) {
                        if (cube_3d[i][j + 1][k + 1] == turn) {
                            if (check_exist(i, j + 2, k + 2)) {
                                if (cube_3d[i][j + 2][k + 2] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([i, (j + 2), (k + 2)])
                                }
                            }
                        }
                    }
                    if (check_exist(i + 1, j - 1, k)) {
                        if (cube_3d[i + 1][j - 1][k] == turn) {
                            if (check_exist(i + 2, j - 2, k)) {
                                if (cube_3d[i + 2][j - 2][k] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([(i + 2), (j - 2), k])
                                }
                            }
                        }
                    }
                    if (check_exist(i + 1, j, k - 1)) {
                        if (cube_3d[i + 1][j][k - 1] == turn) {
                            if (check_exist(i + 2, j, k - 2)) {
                                if (cube_3d[i + 2][j][k - 2] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([(i + 2), j, (k - 2)])
                                }
                            }
                        }
                    }
                    if (check_exist(i, j + 1, k - 1)) {
                        if (cube_3d[i][j + 1][k - 1] == turn) {
                            if (check_exist(i, j + 2, k - 2)) {
                                if (cube_3d[i][j + 2][k - 2] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([i, (j + 2), (k - 2)])
                                }
                            }
                        }
                    }
                    if (check_exist(i + 1, j + 1, k + 1)) {
                        if (cube_3d[i + 1][j + 1][k + 1] == turn) {
                            if (check_exist(i + 2, j + 2, k + 2)) {
                                if (cube_3d[i + 2][j + 2][k + 2] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([(i + 2), (j + 2), (k + 2)])
                                }
                            }
                        }
                    }
                    if (check_exist(i + 1, j - 1, k + 1)) {
                        if (cube_3d[i + 1][j - 1][k + 1] == turn) {
                            if (check_exist(i + 2, j - 2, k + 2)) {
                                if (cube_3d[i + 2][j - 2][k + 2] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([(i + 2), (j - 2), (k + 2)])
                                }
                            }
                        }
                    }
                    if (check_exist(i + 1, j + 1, k - 1)) {
                        if (cube_3d[i + 1][j + 1][k - 1] == turn) {
                            if (check_exist(i + 2, j + 2, k - 2)) {
                                if (cube_3d[i + 2][j + 2][k - 2] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([(i + 2), (j + 2), (k - 2)])
                                }
                            }
                        }
                    }
                    if (check_exist(i - 1, j + 1, k + 1)) {
                        if (cube_3d[i - 1][j + 1][k + 1] == turn) {
                            if (check_exist(i - 2, j + 2, k + 2)) {
                                if (cube_3d[i - 2][j + 2][k + 2] == turn) {
                                    exists.push([i, j, k])
                                    exists.push([(i - 2), (j + 2), (k + 2)])
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return (exists)
}

let turn;
turn = Math.floor(Math.random() * 2);
const controls = new OrbitControls(camera, renderer.domElement);
var cube = [];
var cube_3d = [];
for (let i = 0; i < 3; i++) {
    var tempi = [];
    for (let j = 0; j < 3; j++) {
        var tempj = ['-', '-', '-'];
        tempi[j] = tempj;
    }
    cube_3d[i] = tempi;
}
// console.log(cube_3d);
for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        for (let k = 0; k < 3; k++) {
            if( i == 1 && j ==1 && k == 1){
                const geometry = new THREE.BoxGeometry(0.0, 0.0, 0.0);
                const material = new THREE.MeshLambertMaterial({ color: 0x00ffff });
                material.transparent = true;
                material.opacity = 0.5;
                cube[9 * i + j * 3 + k] = new THREE.Mesh(geometry, material);
                cube[9 * i + j * 3 + k].position.set(i - 1, j - 1, k - 1)
                scene.add(cube[9 * i + j * 3 + k]);
                continue;
            }
            const geometry = new THREE.BoxGeometry(0.35, 0.35, 0.35);
            const edges = new THREE.EdgesGeometry(geometry);
            const line = new THREE.LineSegments(edges, new THREE.LineBasicMaterial({ color: 0x808080 }));
            line.position.set(i - 1, j - 1, k - 1)
            scene.add(line);
            const material = new THREE.MeshLambertMaterial({ color: 0x00ffff });
            material.transparent = true;
            material.opacity = 0.5;
            cube[9 * i + j * 3 + k] = new THREE.Mesh(geometry, material);
            cube[9 * i + j * 3 + k].position.set(i - 1, j - 1, k - 1)
            scene.add(cube[9 * i + j * 3 + k]);

        }
    }
}
// console.log(cube)
camera.position.x = 2.5;
camera.position.y = 2.5;
camera.position.z = 2.5;
// let stats;
// stats = new Stats();
// document.body.appendChild(stats.dom);

window.addEventListener('resize', onWindowResize, false)
function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.setSize(window.innerWidth, window.innerHeight)
    render()
}
document.addEventListener('click', onMouseClick, false);
const buttonRestart = document.getElementById('restart');
buttonRestart.addEventListener('click', function () {
    window.location.reload(true);

});
const buttonMenu = document.getElementById('back_menu');
buttonMenu.addEventListener('click', function () {
    window.location.href="/..";

});
function computer_turn(){    //computer turn

    let end,new_x,new_y,new_z;
    end=0;
    document.removeEventListener('click', onMouseClick, false);
    while(true){
        new_x=Math.floor(Math.random() * 3);
        new_y=Math.floor(Math.random() * 3);
        new_z=Math.floor(Math.random() * 3);
        console.log(new_x,new_y,new_z);
        if(cube_3d[new_x][new_y][new_z]=='-'){
            break;
        }
    }
    cube_3d[new_x][new_y][new_z]=turn;
    const selectedCube=cube[new_x*9+new_y*3+new_z];
    const newMaterial = new THREE.MeshLambertMaterial({ color: 0x0000ff });
    newMaterial.transparent = true;
    newMaterial.opacity = 0.5;
    selectedCube.material = newMaterial;
    const exists = (check_3d_cube(cube_3d, turn));
    console.log(exists)
    if (exists.length != 0) {
        for (let i = 0; i < exists.length; i = i + 2) {
            const material = new THREE.LineBasicMaterial({ color: 0x0000ff });
            material.linewidth = 5;
            const points = [];
            points.push(new THREE.Vector3(exists[i][0] - 1, exists[i][1] - 1, exists[i][2] - 1));
            points.push(new THREE.Vector3(exists[i + 1][0] - 1, exists[i + 1][1] - 1, exists[i + 1][2] - 1));
            const geometry = new THREE.BufferGeometry().setFromPoints(points);
            const line = new THREE.Line(geometry, material);
            scene.add(line);
            document.removeEventListener('click', onMouseClick, false);
            const winner=document.createElement('h1');
            if(turn==0){
                winner.textContent="COMPUTER WON";
            }else{
                winner.textContent="YOU WON";
            }
            const gameover =document.getElementsByClassName("gameover")[0];
            gameover.appendChild(winner);
            gameover.classList.add("gameovervis");
            if(turn==0){
                gameover.style.backgroundColor = "rgba(156, 159, 251, 0.5)";

            }
            end=1;
        }
    }
    turn = (turn + 1) % 2;
    if(end==0){
    document.addEventListener('click', onMouseClick, false);
    }
}

if(turn==0){
    computer_turn();
}
function onMouseClick(event) {
    let end;
    end=0;
    const raycaster = new THREE.Raycaster();
    let setColor;
    setColor = 0xff0000;
    const mouse = new THREE.Vector2(
        (event.clientX / window.innerWidth) * 2 - 1,
        -(event.clientY / window.innerHeight) * 2 + 1
    );


    raycaster.setFromCamera(mouse, camera);

    const intersects = raycaster.intersectObjects(cube);

    if (intersects.length > 0) {
        const selectedCube = intersects[0].object;
        if (cube_3d[selectedCube.position.x + 1][selectedCube.position.y + 1][selectedCube.position.z + 1] == '-') {
            cube_3d[selectedCube.position.x + 1][selectedCube.position.y + 1][selectedCube.position.z + 1] = turn;
            const newMaterial = new THREE.MeshLambertMaterial({ color: setColor });
            newMaterial.transparent = true;
            newMaterial.opacity = 0.5;
            selectedCube.material = newMaterial;
            const exists = (check_3d_cube(cube_3d, turn));
            console.log(exists)
            if (exists.length != 0) {
                for (let i = 0; i < exists.length; i = i + 2) {
                    const material = new THREE.LineBasicMaterial({ color: setColor });
                    material.linewidth = 5;
                    const points = [];
                    points.push(new THREE.Vector3(exists[i][0] - 1, exists[i][1] - 1, exists[i][2] - 1));
                    points.push(new THREE.Vector3(exists[i + 1][0] - 1, exists[i + 1][1] - 1, exists[i + 1][2] - 1));
                    const geometry = new THREE.BufferGeometry().setFromPoints(points);
                    const line = new THREE.Line(geometry, material);
                    scene.add(line);
                    document.removeEventListener('click', onMouseClick, false);
                    const winner=document.createElement('h1');
                    if(turn==0){
                        winner.textContent="COMPUTER WON";
                    }else{
                        winner.textContent="YOU WON";
                    }
                    const gameover =document.getElementsByClassName("gameover")[0];
                    gameover.appendChild(winner);
                    gameover.classList.add("gameovervis");
                    if(turn==0){
                        gameover.style.backgroundColor = "rgba(156, 159, 251, 0.5)";

                    }
                    end=1;
                     
                }
            }
            turn = (turn + 1) % 2;
            if(end==0){
            computer_turn();
            }
        }
    }

}
controls.update()

function animate() {
    requestAnimationFrame(animate);
    controls.update()
    render();
    // stats.update();
}
function render() {

    renderer.render(scene, camera)
}
animate();