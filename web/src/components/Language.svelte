<script lang="ts">
  export let language = '';
  export let small = false;

  interface LanguageAttributes {
    name: string;
    icon: string;
    color: string;
  }

  interface BadgeConfigs {
    [key: string]: LanguageAttributes;
  }

  const badgeConfigs: BadgeConfigs = {
    // Programming Languages
    android:        { name: 'Android',       color: '3DDC84', icon: 'android' },
    astro:          { name: 'Astro',         color: 'E83CB9', icon: 'astro' },
    alpine:         { name: 'Alpine.js',     color: '8BC0D0', icon: 'alpinedotjs' },
    angular:        { name: 'Angular',       color: 'DD0031', icon: 'angular' },
    bash:           { name: 'Bash',          color: '4EAA25', icon: 'gnubash' },
    c:              { name: 'C',             color: 'A8B9CC', icon: 'c' },
    'c++':          { name: 'C++',           color: '00599C', icon: 'cplusplus' },
    'c#':           { name: 'C#',            color: '9B59B6', icon: 'csharp' },
    coffeescript:   { name: 'CoffeeScript',  color: '6F4E37', icon: 'coffeescript' },
    css:            { name: 'CSS',           color: '1572B6', icon: 'css3' },
    d3:             { name: 'D3.js',         color: 'F9A03C', icon: 'd3dotjs' },
    dart:           { name: 'Dart',          color: '0175C2', icon: 'dart' },
    docker:         { name: 'Docker',        color: '2496ED', icon: 'docker' },
    dockerfile:     { name: 'Docker',        color: '2496ED', icon: 'docker' },
    elixir:         { name: 'Elixir',        color: '4B275F', icon: 'elixir' },
    flutter:        { name: 'Flutter',       color: '02569B', icon: 'flutter' },
    git:            { name: 'Git',           color: 'F05032', icon: 'git' },
    go:             { name: 'Go',            color: '00ADD8', icon: 'go' },
    html:           { name: 'HTML',          color: 'E34F26', icon: 'html5' },
    'html/css':     { name: 'HTML/CSS',      color: 'E34F26', icon: 'html5' },
    java:           { name: 'Java',          color: '5382A1', icon: 'openjdk' },
    javascript:     { name: 'JavaScript',    color: 'F7DF1E', icon: 'javascript' },
    julia:          { name: 'Julia',         color: '9558B2', icon: 'julia' },
    kotlin:         { name: 'Kotlin',        color: '7F52FF', icon: 'kotlin' },
    linux:          { name: 'Linux',         color: 'FCC624', icon: 'linux' },
    lit:            { name: 'Lit',           color: '324FFF', icon: 'lit' },
    markdown:       { name: 'Markdown',      color: '888888', icon: 'markdown' },
    net:            { name: '.NET',          color: '512BD4', icon: 'dotnet' },
    node:           { name: 'Node.js',       color: '339933', icon: 'nodedotjs' },
    nodejs:         { name: 'Node.js',       color: '339933', icon: 'nodedotjs' },
    nextjs:         { name: 'Next.js',       color: 'AAAAAA', icon: 'nextdotjs' },
    php:            { name: 'PHP',           color: '777BB4', icon: 'php' },
    powershell:     { name: 'PowerShell',    color: '5391FE', icon: 'powershell' },
    preact:         { name: 'Preact',        color: '673AB8', icon: 'preact' },
    python:         { name: 'Python',        color: '4B8BBE', icon: 'python' },
    react:          { name: 'React',         color: '61DAFB', icon: 'react' },
    reactnative:    { name: 'React Native',  color: '61DAFB', icon: 'react' },
    ruby:           { name: 'Ruby',          color: 'CC342D', icon: 'ruby' },
    rust:           { name: 'Rust',          color: 'E86243', icon: 'rust' },
    scala:          { name: 'Scala',         color: 'DC322F', icon: 'scala' },
    shell:          { name: 'Shell',         color: '4EAA25', icon: 'gnubash' },
    svelte:         { name: 'Svelte',        color: 'FF3E00', icon: 'svelte' },
    swift:          { name: 'Swift',         color: 'F05138', icon: 'swift' },
    typescript:     { name: 'TypeScript',    color: '3178C6', icon: 'typescript' },
    vue:            { name: 'Vue.js',        color: '4FC08D', icon: 'vuedotjs' },

    // DevOps & Tools
    ansible:        { name: 'Ansible',        color: 'EE0000', icon: 'ansible' },
    kubernetes:     { name: 'Kubernetes',     color: '326CE5', icon: 'kubernetes' },
    githubactions:  { name: 'GitHub Actions', color: '2088FF', icon: 'githubactions' },
    terraform:      { name: 'Terraform',      color: '844FBA', icon: 'terraform' },
    prometheus:     { name: 'Prometheus',     color: 'E6522C', icon: 'prometheus' },
    grafana:        { name: 'Grafana',        color: 'F46800', icon: 'grafana' },

    // Cloud
    netlify:        { name: 'Netlify',   color: '00C7B7', icon: 'netlify' },
    vercel:         { name: 'Vercel',    color: 'AAAAAA', icon: 'vercel' },
    cloudflare:     { name: 'Cloudflare', color: 'F38020', icon: 'cloudflare' },
    aws:            { name: 'AWS',       color: 'FF9900', icon: 'amazonwebservices' },
    azure:          { name: 'Azure',     color: '0089D6', icon: 'microsoftazure' },
    gcp:            { name: 'GCP',       color: '4285F4', icon: 'googlecloud' },

    // Databases
    mysql:          { name: 'MySQL',        color: '4479A1', icon: 'mysql' },
    mssql:          { name: 'MSSQL',        color: 'CC2927', icon: 'microsoftsqlserver' },
    mongodb:        { name: 'MongoDB',      color: '47A248', icon: 'mongodb' },
    redis:          { name: 'Redis',        color: 'DC382D', icon: 'redis' },
    sqlite:         { name: 'SQLite',       color: '44A8E0', icon: 'sqlite' },
    postgresql:     { name: 'PostgreSQL',   color: '336791', icon: 'postgresql' },
    entityframework:{ name: 'Entity Framework', color: '512BD4', icon: 'dotnet' },

    // Security
    burpsuite:      { name: 'Burp Suite',          color: 'FF6633', icon: '' },
    owasp:          { name: 'OWASP',               color: 'F3881D', icon: 'owasp' },
    wireshark:      { name: 'Wireshark',           color: '1679A7', icon: 'wireshark' },
    hackthebox:     { name: 'Hack The Box',        color: '9FEF00', icon: 'hackthebox' },
    bugbounty:      { name: 'Bug Bounty',          color: '00C244', icon: '' },
    vulnerabilityresearch: { name: 'Vulnerability Research', color: 'E74C3C', icon: '' },
    restapis:       { name: 'REST APIs',           color: '0096D6', icon: '' },
    nmap:           { name: 'Nmap',                color: '4F5D95', icon: '' },
  };

  const getLangAttributes = (lang: string): LanguageAttributes => {
    const key = lang?.toLocaleLowerCase().replaceAll('.', '').replaceAll(' ', '');
    return badgeConfigs[key] || { name: lang, color: 'AAAAAA', icon: '' };
  };

  $: langAttributes = getLangAttributes(language);
</script>

{#if langAttributes}
<div
  class="language {small ? 'small' : ''}"
  title={langAttributes.name}
  style="--lang-color: #{langAttributes.color};"
>
  {#if langAttributes.icon}
    <img
      height="16" width="16" alt=""
      src="https://cdn.simpleicons.org/{langAttributes.icon}/{langAttributes.color}"
    />
  {/if}
  {langAttributes.name}
</div>
{/if}

<style lang="scss">
  img {
    transition: transform 0.1s ease-in-out;
    filter: brightness(1.8);
    vertical-align: middle;
    &:hover { transform: scale(1.05); }
  }

  .language {
    font-size: 0.95rem;
    font-weight: 500;
    width: fit-content;
    padding: 0.15rem 0.4rem;
    border-radius: 4px;
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    transition: all 0.2s ease-in-out;
    cursor: default;
    color: var(--lang-color);
    filter: brightness(1.6);
    border: 1px solid color-mix(in srgb, var(--lang-color) 25%, transparent);
    background: color-mix(in srgb, var(--lang-color) 8%, transparent);

    &:hover {
      filter: brightness(2);
      background: color-mix(in srgb, var(--lang-color) 15%, transparent);
    }

    &.small {
      font-size: 0.8rem;
      font-weight: 400;
      img { width: 0.8rem; height: 0.8rem; }
    }
  }
</style>
