const apiUrlMemberGetMember = 'http://127.0.0.1:8000/api/member_get/';
const apiUrlFeedback = 'http://127.0.0.1:8000/api/feedbacks/';

async function fetchConvites() {
    try {
        const response = await fetch(apiUrlMemberGetMember, {
            method: 'GET',
            headers: {
                'Authorization': 'Token c1c82e123abc123abcde4567def01234abcd5678',
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
        const data = await response.json();
        const contentTable = document.querySelector("#conviteTable tbody");
        contentTable.innerHTML = "";

        data.forEach((content) => {
            const row = `
                <tr>
                    <td>${content.link}</td>
                    <td>${content.userRemetente}</td>
                    <td>${content.userDestinatario}</td>
                    <td>${content.data_envio}</td>
                    <td>${content.status}</td>
                </tr>
            `;
            contentTable.innerHTML += row;
        });
    } catch (error) {
        console.error("Erro ao buscar conteúdos:", error);
    }
}

async function fetchFeedbacks() {
    try {
        const response = await fetch(apiUrlFeedback, {
            method: 'GET',
            headers: {
                'Authorization': 'Token c1c82e123abc123abcde4567def01234abcd5678',
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
        const data = await response.json();
        const contentTable = document.querySelector("#feedbackTable tbody");
        contentTable.innerHTML = "";

        data.forEach((content) => {
            const row = `
                <tr>
                    <td>${content.id}</td>
                    <td>${content.feedback}</td>
                    <td>${content.tipo}</td>
                    <td>${content.data}</td>
                    <td>${content.member}</td>
                </tr>
            `;
            contentTable.innerHTML += row;
        });
    } catch (error) {
        console.error("Erro ao buscar conteúdos:", error);
    }
}

document.addEventListener('DOMContentLoaded', fetchConvites);
document.addEventListener('DOMContentLoaded', fetchFeedbacks);
document.getElementById("inviteForm").addEventListener("submit", addConvite);
document.getElementById("feedbackForm").addEventListener("submit", addFeedback);
